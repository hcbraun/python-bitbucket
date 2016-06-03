# -*- coding: utf-8 -*-
URLS = {
    # Issue comments
    'GET_COMMENTS': 'repositories/%(username)s/%(repo_slug)s/pullrequests/%(pullrequest_id)s/comments/',
    'GET_COMMENT': 'repositories/%(username)s/%(repo_slug)s/pullrequests/%(pullrequest_id)s/comments/%(comment_id)s/',
    'CREATE_COMMENT': 'repositories/%(username)s/%(repo_slug)s/pullrequests/%(pullrequest_id)s/comments/',
    'UPDATE_COMMENT': 'repositories/%(username)s/%(repo_slug)s/pullrequests/%(pullrequest_id)s/comments/%(comment_id)s/',
    'DELETE_COMMENT': 'repositories/%(username)s/%(repo_slug)s/pullrequests/%(pullrequest_id)s/comments/%(comment_id)s/',
}


class PullRequestComment(object):
    """ This class provide PullRequest's comments related methods to Bitbucket objects."""

    def __init__(self, pullrequest):
        self.pullrequest = pullrequest
        self.bitbucket = self.pullrequest.bitbucket
        self.bitbucket.URLS.update(URLS)
        self.pullrequest_id = pullrequest.pullrequest_id

    def all(self, pullrequest_id=None, repo_slug=None):
        """ Get PullRequest comments from one of your repositories.
        """
        pullrequest_id = pullrequest_id or self.pullrequest_id
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url('GET_COMMENTS',
                                 username=self.bitbucket.username,
                                 repo_slug=repo_slug,
                                 pullrequest_id=pullrequest_id)
        return self.bitbucket.dispatch('GET', url, auth=self.bitbucket.auth)

    def get(self, comment_id, pullrequest_id=None, repo_slug=None):
        """ Get a PullRequest from one of your repositories.
        """
        pullrequest_id = pullrequest_id or self.pullrequest_id
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url('GET_COMMENT',
                                 username=self.bitbucket.username,
                                 repo_slug=repo_slug,
                                 pullrequest_id=pullrequest_id,
                                 comment_id=comment_id)
        return self.bitbucket.dispatch('GET', url, auth=self.bitbucket.auth)

    def create(self, pullrequest_id=None, repo_slug=None, **kwargs):
        """ Add a PullRequest comment to one of your repositories.
            Each PullRequest comment require only the content data field
            the system autopopulate the rest.
        """
        pullrequest_id = pullrequest_id or self.pullrequest_id
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url('CREATE_COMMENT',
                                 username=self.bitbucket.username,
                                 repo_slug=repo_slug,
                                 pullrequest_id=pullrequest_id)
        return self.bitbucket.dispatch('POST', url, auth=self.bitbucket.auth, **kwargs)

    def update(self, comment_id, pullrequest_id=None, repo_slug=None, **kwargs):
        """ Update a PullRequest comment in one of your repositories.
            Each PullRequest comment require only the content data field
            the system autopopulate the rest.
        """
        pullrequest_id = pullrequest_id or self.pullrequest_id
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url('UPDATE_COMMENT',
                                 username=self.bitbucket.username,
                                 repo_slug=repo_slug,
                                 pullrequest_id=pullrequest_id,
                                 comment_id=comment_id)
        return self.bitbucket.dispatch('PUT', url, auth=self.bitbucket.auth, **kwargs)

    def delete(self, comment_id, pullrequest_id=None, repo_slug=None):
        """ Delete a PullRequest from one of your repositories.
        """
        pullrequest_id = pullrequest_id or self.pullrequest_id
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url('DELETE_COMMENT',
                                 username=self.bitbucket.username,
                                 repo_slug=repo_slug,
                                 pullrequest_id=pullrequest_id,
                                 comment_id=comment_id)
        return self.bitbucket.dispatch('DELETE', url, auth=self.bitbucket.auth)
