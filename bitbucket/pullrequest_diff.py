# -*- coding: utf-8 -*-

URLS = {
    # Get Diff
    'GET_DIFF': 'repositories/%(username)s/%(repo_slug)s/pullrequests/%(pullrequest_id)s/diff/',
}


class PullRequestDiff(object):
    """
    This class provide PullRequest's changesets related methods
    to Bitbucket objects.
    """

    def __init__(self, pullrequest):
        self.pullrequest = pullrequest
        self.bitbucket = self.pullrequest.bitbucket
        self.bitbucket.URLS.update(URLS)
        self.pullrequest_id = pullrequest.pullrequest_id

    def get(self, pullrequest_id=None, repo_slug=None):
        """
        Get a PullRequest from one of your repositories.
        """
        pullrequest_id = pullrequest_id or self.pullrequest_id
        repo_slug = repo_slug or self.bitbucket.repo_slug or ''
        url = self.bitbucket.url_v2('GET_DIFF',
                                    username=self.bitbucket.username,
                                    repo_slug=repo_slug,
                                    pullrequest_id=pullrequest_id)

        success, diff = self.bitbucket.dispatch('GET', url,
                                                auth=self.bitbucket.auth)
        if success:
            # request succeed, return diff
            return diff
        else:
            # request failed
            return None
