# Back-end Challenge
# In the Bash script, write a program that creates a file named Dockerfile. The contents of the Dockerfile should have the following commands:
# ﻿﻿﻿Set the base image to redis: 7. 0.11
# ﻿﻿﻿Install the necessary dependencies for Redis Cluster management, including curl and redis-tools.
# ﻿﻿﻿Set the working directory to / redis.
# ﻿﻿﻿Copy the nodes. conf file from the current directory to the working directory.
# ﻿﻿﻿Set the redis. conf file to use a custom configuration file named cluster-redis. conf from the current directory.
# ﻿﻿﻿Set an environment variable named REDIS_ENV with the value cluster.
# ﻿﻿﻿Create a directory named /data to be used as a Redis data directory.
# ﻿﻿﻿Set the user to run the Redis server as redis.
# ﻿﻿﻿Expose ports 7000 to 7005 for the Redis Cluster nodes.
# ﻿﻿﻿﻿Add a script cluster-init. sh from the current directory and set it as an entrypoint.
# Print the contents of your Dockerfile at the end.

#!/bin/bash

#!/bin/bash

cat <<EOF > Dockerfile
FROM redis:7.0.11
RUN apt-get update && apt-get install -y curl redis-tools && rm -rf /var/lib/apt/lists/*
WORKDIR /redis
COPY nodes.conf /redis/
COPY cluster-redis.conf /redis/redis.conf
ENV REDIS_ENV cluster
RUN mkdir /data
RUN chown redis:redis /data
EXPOSE 7000-7005
COPY cluster-init.sh /usr/local/bin/
ENTRYPOINT ["cluster-init.sh"]
EOF

# Print the contents of Dockerfile
cat Dockerfile
