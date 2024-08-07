"""
Facebook API CRUD Operations Module

This module provides functions to perform CRUD operations on Facebook posts using the Graph API.

Functions:
    create_post(message, image_url=None): Creates a post on the Facebook page.
    read_post(post_id): Reads a post from the Facebook page.
    update_post(post_id, message): Updates a post on the Facebook page.
    delete_post(post_id): Deletes a post from the Facebook page.
"""

# Third party library imports
import requests

# Standard Imports
import copy


# Local imports
from logging_package.logging_utility import *
from email_setup.email_operations import notify_failure, notify_success
import constants as C


def create_post(caption, image_url=None):
    """
    Create a post on the Facebook page.

    :param caption: The caption to post.
    :param image_url: The URL of the image to include in the post (optional).
    :return: The response from the API.
    """
    log_info(f"Function create_post started with caption: {caption}, image_url: {image_url}")

    payload = copy.deepcopy(C.PAYLOAD)
    payload['message'] = caption  # Use 'message' instead of 'caption'
    if image_url:
        payload['url'] = image_url

    url = f"{C.FACEBOOK_GRAPH_URL}{C.API_VERSION}/{C.PAGE_ID}/photos?access_token={C.ACCESS_TOKEN}" if image_url else \
        f"{C.FACEBOOK_GRAPH_URL}{C.API_VERSION}/{C.PAGE_ID}/feed?access_token={C.ACCESS_TOKEN}"

    log_info(f"Creating post with payload: {payload}")

    try:
        response = requests.post(url, headers=C.HEADERS, json=payload)
        response.raise_for_status()
        log_info(f"Post created successfully: {response.json()}")
        notify_success("Post Created", f"Post created successfully: {response.json()}")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        log_error(f"HTTP error occurred: {http_err}")
        log_debug(f"Response Content: {response.content}")
        notify_failure("Post Creation Failed", f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        log_error(f"An error occurred: {err}")
        notify_failure("Post Creation Failed", f"An error occurred: {err}")
        raise
    finally:
        log_info("Function create_post completed")


def read_post(post_id):
    """
    Read a post from the Facebook page.

    :param post_id: The ID of the post to read.
    :return: The response from the API.
    """
    log_debug(f"Function read_post started with post_id: {post_id}")

    url = f"{C.FACEBOOK_GRAPH_URL}{C.API_VERSION}/{C.PAGE_ID}_{post_id}?access_token={C.ACCESS_TOKEN}"

    log_debug(f"Reading post with ID: {post_id}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        log_info(f"Post retrieved successfully: {response.json()}")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        log_error(f"HTTP error occurred: {http_err}")
        log_debug(f"Response Content: {response.content}")
        notify_failure("Post Reading Failed", f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        log_error(f"An error occurred: {err}")
        notify_failure("Post Reading Failed", f"An error occurred: {err}")
        raise
    finally:
        log_debug("Function read_post completed")


def update_post(post_id, caption):
    """
    Update a post on the Facebook page.

    :param post_id: The ID of the post to update.
    :param caption: The new caption to update the post with.
    :return: The response from the API.
    """
    log_debug(f"Function update_post started with post_id: {post_id}, caption: {caption}")

    url = f"{C.FACEBOOK_GRAPH_URL}{C.API_VERSION}/{C.PAGE_ID}_{post_id}?access_token={C.ACCESS_TOKEN}"
    payload = {
        'message': caption  # Use 'message' instead of 'caption'
    }

    log_debug(f"Updating post with ID: {post_id} and payload: {payload}")

    try:
        response = requests.post(url, headers=C.HEADERS, json=payload)
        response.raise_for_status()
        log_info(f"Post updated successfully: {response.json()}")
        notify_success("Post Updated", f"Post updated successfully: {response.json()}")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        log_error(f"HTTP error occurred: {http_err}")
        log_debug(f"Response Content: {response.content}")
        notify_failure("Post Update Failed", f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        log_error(f"An error occurred: {err}")
        notify_failure("Post Update Failed", f"An error occurred: {err}")
        raise
    finally:
        log_debug("Function update_post completed")


def delete_post(post_id):
    """
    Delete a post from the Facebook page.

    :param post_id: The ID of the post to delete.
    :return: The response from the API.
    """
    log_debug(f"Function delete_post started with post_id: {post_id}")

    url = f"{C.FACEBOOK_GRAPH_URL}{C.API_VERSION}/{C.PAGE_ID}_{post_id}?access_token={C.ACCESS_TOKEN}"

    log_debug(f"Deleting post with ID: {post_id}")

    try:
        response = requests.delete(url)
        response.raise_for_status()
        log_info(f"Post deleted successfully: {response.json()}")
        notify_success("Post Deleted", f"Post deleted successfully: {response.json()}")
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        log_error(f"HTTP error occurred: {http_err}")
        log_debug(f"Response Content: {response.content}")
        notify_failure("Post Deletion Failed", f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        log_error(f"An error occurred: {err}")
        notify_failure("Post Deletion Failed", f"An error occurred: {err}")
        raise
    finally:
        log_debug("Function delete_post completed")


def main():
    """
    Main function to perform CRUD operations on Facebook posts.
    """
    log_debug("Function main started")

    # Create a new post
    try:
        create_response = create_post(caption=C.CAPTION, image_url=C.IMAGE_URL)
        post_id = create_response['id']
    except Exception as e:
        log_error(f"Failed to create post: {e}")
        return

    # Read the created post
    try:
        read_response = read_post(post_id)
    except Exception as e:
        log_error(f"Failed to read post: {e}")
        return

    # Update the post
    try:
        update_response = update_post(post_id, "Hello, updated world!")
    except Exception as e:
        log_error(f"Failed to update post: {e}")
        return

    # Delete the post
    try:
        delete_response = delete_post(post_id)
    except Exception as e:
        log_error(f"Failed to delete post: {e}")
        return

    log_debug("Function main completed")


if __name__ == "__main__":
    main()
