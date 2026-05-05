"""Constants for the Yarbo HA integration."""

DOMAIN = "yarboha"
PLATFORMS = ["sensor", "binary_sensor", "select", "device_tracker", "button", "switch", "number"]

# Config flow
CONF_EMAIL = "email"
CONF_PASSWORD = "password"
# Config entry data keys
DATA_ACCESS_TOKEN = "access_token"
DATA_REFRESH_TOKEN = "refresh_token"

# Options
CONF_SELECTED_DEVICES = "selected_devices"
