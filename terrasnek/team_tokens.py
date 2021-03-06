"""
Module for Terraform Cloud API Endpoint: Team Tokens.
"""

from .endpoint import TFCEndpoint
from ._constants import Entitlements

class TFCTeamTokens(TFCEndpoint):
    """
    `API Docs \
        <https://www.terraform.io/docs/cloud/api/team-tokens.html>`_
    """

    def __init__(self, instance_url, org_name, headers, well_known_paths, verify, log_level):
        super().__init__(instance_url, org_name, headers, well_known_paths, verify, log_level)
        self._endpoint_base_url = f"{self._api_v2_base_url}/teams"

    def required_entitlements(self):
        return [Entitlements.TEAMS]

    def create(self, team_id, payload=None):
        """
        ``POST /teams/:team_id/authentication-token``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/team-tokens.html#generate-a-new-team-token>`_
        """

        if payload is None:
            payload = {}

        url = f"{self._endpoint_base_url}/{team_id}/authentication-token"
        return self._create(url, payload=payload)


    def destroy(self, team_id):
        """
        ``DELETE /teams/:team_id/authentication-token``

        `API Doc Reference \
            <https://www.terraform.io/docs/cloud/api/team-tokens.html#delete-the-team-token>`_
        """
        url = f"{self._endpoint_base_url}/{team_id}/authentication-token"
        return self._destroy(url)
