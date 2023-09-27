import multiprocessing

# Use threaded workers. Thread-based concurrency is provided via the 'futures'
# package. 'gevent' or other workers would be candidates, except that the ndb
# library has its own concurrency model that conflicts with gevent and possibly
# with similar approaches.
worker_class = 'gthread'

# Use a number of workers equal to the number of CPU cores available.
# Reducing this number on a multicore instance will reduce memory consumption,
# but will also reduce the app's ability to utilize all available CPU resources.
# workers = multiprocessing.cpu_count()
workers = 4 # good

# Use an arbitrary number of threads for concurrency. This will dictate the
# maximum number of requests handled concurrently by EACH worker.
threads = 6

# The maximum number of requests a worker will process before restarting.
# Any value greater than zero will limit the number of requests a worker will process
# before automatically restarting. This is a simple method to help limit the damage of memory leaks.
max_requests = 5

# The maximum jitter to add to the max_requests setting.
# The jitter causes the restart per worker to be randomized by
# randint(0, max_requests_jitter). This is intended to stagger worker
# restarts to avoid all workers restarting at the same time.
max_requests_jitter = 2

# Workers silent for more than this many seconds are killed and restarted.
# Value is a positive number or 0. Setting it to 0 has the effect of infinite
# timeouts by disabling timeouts for all workers entirely.
timeout = 30

# Settings specific to the Managed VMs production environment such as "bind"
# and "logfile" are set in the Dockerfile's ENTRYPOINT directive.

# Store the process ID of gunicorn.  Used for testing.
pidfile = 'gunicorn_pid.txt'

# use: gunicorn -b :$PORT -c gunicorn.conf.py app:app
