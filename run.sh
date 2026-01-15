sudo .docker . run. -d . \
- -hostname rabbitmq \
-log-driver=journald
-- name.rabbitmq \
-p .5672 : 5672 . \
p.15672 : 15672 \
-p . 15674: 15674
-p. 25672 : 25672 \
-p.61613 : 61613 \
-V. rabbitmq_data:/var/lib/rabbitmq \
rabbitmq:3.6.14-management
