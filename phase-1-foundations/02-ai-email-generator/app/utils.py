def format_response(email_content: str):
    """
    Format email response
    :param email_content: Email content
    :return: JSON response
    """

    return {
        "generated_email": email_content
    }
