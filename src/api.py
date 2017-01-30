from app import app, cache
from flask import request
from flask_peewee.rest import RestAPI, RestResource
from flask_peewee.utils import get_object_or_404
from models import Person

api = RestAPI(app)


class CachedRestResource(RestResource):
    @cache.cached(timeout=10)
    def get_cached(self, pk):
        obj = get_object_or_404(self.get_query(), self.pk == pk)
        return self.object_detail(obj)

    def api_detail(self, pk, method=None):

        method = method or request.method

        if method == 'GET':
            return self.get_cached(pk)

        obj = get_object_or_404(self.get_query(), self.pk == pk)
        if not getattr(self, 'check_%s' % method.lower())(obj):
            return self.response_forbidden()

        if method in ('PUT', 'POST'):
            return self.edit(obj)
        elif method == 'DELETE':
            return self.delete(obj)


class PersonResource(CachedRestResource):
    paginate_by = None


from auth import NoAuth

api.register(Person, PersonResource, auth=NoAuth)
