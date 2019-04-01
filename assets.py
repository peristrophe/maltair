
import json
from datetime import datetime

from .models import *

class AssetsScanner:

    def channels(self, **kwargs):
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)

        params = {
            'name': name,
            'offset': offset if name is None else None,
            'maxReturn': size if name is None else None,
        }

        if name is not None:
            apipath = '/rest/asset/v1/channel/byName.json'
        else:
            apipath = '/rest/asset/v1/channels.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params))

        if not res['success']:
            raise RuntimeError(res)

        return [ Channel(r, self) for r in res.get('result', []) ]


    def email_templates(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')

        args = {}
        params = {
            'name': name if _id is None else None,
            'status': status,
            'offset': offset if _id is name is None else None,
            'maxReturn': size if _id is name is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/emailTemplate/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/emailTemplate/byName.json'
        else:
            apipath = '/rest/asset/v1/emailTemplates.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ EmailTemplate(r, self) for r in res.get('result', []) ]


    def emails(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')
        folder = kwargs.get('folder')

        args = {}
        params = {
            'name': name if _id is None else None,
            'folder': folder if _id is None else None,
            'status': status,
            'offset': offset if _id is name is None else None,
            'maxReturn': size if _id is name is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/email/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/email/byName.json'
        else:
            apipath = '/rest/asset/v1/emails.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ Email(r, self) for r in res.get('result', []) ]


    def files(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        folder = kwargs.get('folder')

        args = {}
        params = {
            'name': name if _id is None else None,
            'folder': folder if _id is name is None else None,
            'offset': offset if _id is name is None else None,
            'maxReturn': size if _id is name is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/file/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/file/byName.json'
        else:
            apipath = '/rest/asset/v1/files.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ File(r, self) for r in res.get('result', []) ]


    def folders(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        root = kwargs.get('root')
        _type = kwargs.get('type')
        depth = kwargs.get('maxDepth')
        ws = kwargs.get('workSpace')

        args = {}
        params = {
            'root': root if _id is None else None,
            'type': _type if _id is name is None else None,
            'maxDepth': depth if _id is name is None else None,
            'workSpace': ws if _id is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/folder/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/folder/byName.json'
        else:
            apipath = '/rest/asset/v1/folders.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ Folder(r, self) for r in res.get('result', []) ]


    def forms(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')
        folder = kwargs.get('folder')

        args = {}
        params = {
            'name': name if _id is None else None,
            'folder': folder if _id is None else None,
            'status': status,
            'offset': offset if _id is name is None else None,
            'maxReturn': size if _id is name is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/form/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/form/byName.json'
        else:
            apipath = '/rest/asset/v1/forms.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ Form(r, self) for r in res.get('result', []) ]


    def form_fields(self, **kwargs):
        _id = kwargs.get('id')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')

        args = {}
        params = {
            'status': status if _id is not None else None,
            'offset': offset if _id is None else None,
            'maxReturn': size if _id is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/form/{id}/fields.json'
        else:
            apipath = '/rest/asset/v1/form/fields.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ FormField(r, self) for r in res.get('result', []) ]


    def landing_page_templates(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')
        folder = kwargs.get('folder')

        args = {}
        params = {
            'name': name if _id is None else None,
            'folder': folder if _id is name is None else None,
            'status': status if name is None else None,
            'offset': offset if _id is name is None else None,
            'maxReturn': size if _id is name is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/landingPageTemplate/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/landingPageTemplate/byName.json'
        else:
            apipath = '/rest/asset/v1/landingPageTemplates.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ LandingPageTemplate(r, self) for r in res.get('result', []) ]


    def landing_pages(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')
        folder = kwargs.get('folder')

        args = {}
        params = {
            'name': name if _id is None else None,
            'folder': folder if _id is name is None else None,
            'status': status,
            'offset': offset if _id is None else None,
            'maxReturn': size if _id is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/landingPage/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/landingPage/byName.json'
        else:
            apipath = '/rest/asset/v1/landingPages.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ LandingPage(r, self) for r in res.get('result', []) ]


    def programs(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        tag_type = kwargs.get('tagType')
        tag_value = kwargs.get('tagValue') if tag_type is not None else None
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')
        hastags = kwargs.get('includeTags', False)
        hascosts = kwargs.get('includeCosts', False)
        filter_type = kwargs.get('filterType')
        filter_values = kwargs.get('filterValues') if filter_type is not None else None
        start_date = kwargs.get('earliestUpdatedAt')
        end_date = kwargs.get('latestUpdatedAt')

        args = {}
        params = {
            'name': name if _id is tag_type is None else None,
            'includeTags': hastags if _id is tag_type is None else None,
            'includeCosts': hascosts if _id is tag_type is None else None,
            'tag_type': tag_type if _id is name is None else None,
            'tag_value': tag_value if _id is name is None else None,
            'offset': offset if _id is name is None else None,
            'maxReturn': size if _id is name is None else None,
            'filterType': filter_type if _id is name is tag_type is None else None,
            'filterValues': filter_values if _id is name is tag_type is None else None,
            'earliestUpdatedAt': start_date if _id is name is tag_type is None else None,
            'latestUpdatedAt': end_date if _id is name is tag_type is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/program/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/program/byName.json'
        elif tag_type is not None:
            apipath = '/rest/asset/v1/program/byTag.json'
        else:
            apipath = '/rest/asset/v1/programs.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ Program(r, self) for r in res.get('result', []) ]


    def segments(self, **kwargs):
        status = kwargs.get('status')

        params = {
            'status': status,
        }

        res = json.loads(self._send_req('/rest/asset/v1/segmentation.json', method='GET', params=params,))

        if not res['success']:
            raise RuntimeError(res)

        return [ Segment(r, self) for r in res.get('result', []) ]


    def smart_lists(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        folder = kwargs.get('folder')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)

        args = {}
        params = {
            'folder': folder,
            'name': name if _id is None else None,
            'offset': offset if _id is name is None else None,
            'maxReturn': size if _id is name is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/smartList/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/smartList/byName.json'
        else:
            apipath = '/rest/asset/v1/smartLists.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ SmartList(r, self) for r in res.get('result', []) ]


    def snippets(self, **kwargs):
        _id = kwargs.get('id')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        status = kwargs.get('status')

        args = {}
        params = {
            'status': status,
            'offset': offset if _id is None else None,
            'maxReturn': size if _id is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/snippet/{id}.json'
        else:
            apipath = '/rest/asset/v1/snippets.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ Snippet(r, self) for r in res.get('result', []) ]


    def static_lists(self, **kwargs):
        _id = kwargs.get('id')
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)
        folder = kwargs.get('folder')
        start_date = kwargs.get('earliestUpdatedAt')
        end_date = kwargs.get('latestUpdatedAt')

        args = {}
        params = {
            'name': name if _id is None else None,
            'folder': folder if _id is name is None else None,
            'offset': offset if _id is None else None,
            'maxReturn': size if _id is None else None,
            'earliestUpdatedAt': start_date if _id is name is None else None,
            'latestUpdatedAt': end_date if _id is name is None else None,
        }

        if _id is not None:
            args.update({ 'id': _id })
            apipath = '/rest/asset/v1/staticList/{id}.json'
        elif name is not None:
            apipath = '/rest/asset/v1/staticList/byName.json'
        else:
            apipath = '/rest/asset/v1/staticLists.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params, **args))

        if not res['success']:
            raise RuntimeError(res)

        return [ StaticList(r, self) for r in res.get('result', []) ]


    def tags(self, **kwargs):
        name = kwargs.get('name')
        page = kwargs.get('page', 1)
        size = kwargs.get('maxReturn', 200)
        offset = size * (page - 1)

        params = {
            'name': name,
            'offset': offset if name is None else None,
            'maxReturn': size if name is None else None,
        }

        if name is not None:
            apipath = '/rest/asset/v1/tagType/byName.json'
        else:
            apipath = '/rest/asset/v1/tagTypes.json'

        res = json.loads(self._send_req(apipath, method='GET', params=params))

        if not res['success']:
            raise RuntimeError(res)

        return [ Tag(r, self) for r in res.get('result', []) ]


