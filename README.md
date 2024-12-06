# aws-scps-for-sandbox-and-training-accounts

Collection of example Service Control Policies (SCPs) that are useful for sandbox and training AWS accounts. The SCPs deny API calls that
* change baseline account settings (contacts, billing, tax settings, etc.),
* have long-term financial effects (purchases and reservations) or
* operate outside allow-listed AWS regions or services.


## Notes

* The provided SCPs can only be a starting point and you will need to adapt them for your specific use case.

* Consider using [aws-nuke](https://github.com/ekristen/aws-nuke) to bring AWS accounts back into a clean and known-good state.

* Have a look at the following resources for additional SCPs you might want to implement:
  * https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples.html
  * https://www.wiz.io/blog/using-service-control-policies-to-protect-security-baselines
  * https://www.wiz.io/blog/how-to-set-secure-defaults-on-aws
