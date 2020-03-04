<img src="https://i.ibb.co/QYHDXJ9/simbution.png" align="left"
     title="simbution logo" width="200"><br/>

# What it does
Simbution simulates github contributions to keep the contribution graph green. To do this, it opens an issue via the GitHub API v3 and closes it immediately afterwards. To avoid manual execution of the program simbution is implemented as an aws-lambda-service which is executed daily via a CloudWatch event.