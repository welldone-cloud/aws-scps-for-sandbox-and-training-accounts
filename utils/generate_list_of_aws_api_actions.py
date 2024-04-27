#!/usr/bin/env python3

import datetime
import json
import requests


AWS_POLICY_EDITOR_JS_URL = "https://awspolicygen.s3.amazonaws.com/js/policies.js"

AWS_POLICY_EDITOR_JS_CONFIG_PREFIX = "app.PolicyEditorConfig="

TIMESTAMP_FORMAT = "%Y%m%d%H%M%S"


if __name__ == "__main__":
    policy_editor_js_response = requests.get(AWS_POLICY_EDITOR_JS_URL).text
    policy_editor_js_response = policy_editor_js_response.removeprefix(AWS_POLICY_EDITOR_JS_CONFIG_PREFIX)

    policy_data = json.loads(policy_editor_js_response)
    all_api_actions = []
    for service in policy_data["serviceMap"]:
        for action in policy_data["serviceMap"][service]["Actions"]:
            all_api_actions.append("{}:{}".format(policy_data["serviceMap"][service]["StringPrefix"], action))

    timestamp = datetime.datetime.now(datetime.timezone.utc).strftime(TIMESTAMP_FORMAT)
    result_file = "aws_api_actions_{}.txt".format(timestamp)
    with open(result_file, "w") as out_file:
        for line in sorted(all_api_actions):
            out_file.write("{}\n".format(line))

    print("Results written to {}".format(result_file))
