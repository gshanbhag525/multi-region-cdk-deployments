When running CDK commands, pass the command line flag `-c ctxgroup=group_name_here` to activate a specific context group. If you do not specify one, then the default configured in `cdk.json` is used as the fallback.

Full example: 

`cdk --profile my_profile -c ctxgroup=dev synth`

If you did not provide a default name, and did not specify one on the command line, then an error condition will be raised.


#Additional Topics

Shared Values
It is not unusual to have values that are useful in all environments. This is particular true of cross-account resources.

You can define a special context group named all, and those keys and values will be automatically included with any other context group activated by name.

Example in `cdk.json`:

```json
{
  "context": {
    "contextGroups": {
      "default": "dev",
      "all": {
        "some_shared_efs_id": "fs-00112233"
      },
      "dev": {
        "account_id": "****",
        "em_instance_type": "t3.large",
        "vpc_id": "vpc-*****************"
      },
      "prod": {
        "account_id": "****",
        "em_instance_type": "r5.large",
        "vpc_id": "vpc-*****************"        
      } 
    }
  }
}
```