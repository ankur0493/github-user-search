GITHUB_API_BASE_URL = "https://api.github.com"

GITHUB_SEARCH_BASE_URL = GITHUB_API_BASE_URL + "/search"

GITHUB_USER_LIST_URL = GITHUB_API_BASE_URL + "/users"

GITHUB_USER_DETAIL_URL = GITHUB_USER_LIST_URL + "/{username}"

GITHUB_USER_SEARCH_URL = GITHUB_SEARCH_BASE_URL + "/users"

GITHUB_USER_LIST_ATTRIBUTE_MAP = {
    "login": "username",
    "id": "github_id",
    "type": "user_type",
    "site_admin": "is_site_admin",
    "name": "user_profile_name",
    "hireable": "available_for_hire",
    "created_at": "github_user_created",
    "updated_at": "github_user_updated",
}
