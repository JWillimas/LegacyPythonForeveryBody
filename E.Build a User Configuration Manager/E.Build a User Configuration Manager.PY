#------------------------------------------------------------------
# Create the dictionary

test_settings = {
    "theme": "light"
}

# Add a setting
def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


# Update a setting
def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


# Delete a setting
def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"


# View all settings (fixed: deterministic order and guaranteed trailing newline)
def view_settings(settings):
    if not settings:
        return "No settings available."

    lines = []
    for key in settings:                # stable, deterministic order
        lines.append(f"{key.capitalize()}: {settings[key]}")

    return 'Current User Settings:\n'+"\n".join(lines) + "\n"              # always end with a newline


print(view_settings({'theme': 'dark', 
'notifications':'enabled',
'volume': 'high'
}))

