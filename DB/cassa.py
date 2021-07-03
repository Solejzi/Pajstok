from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.policies import WhiteListRoundRobinPolicy, DowngradingConsistencyRetryPolicy,ConsistencyLevel
from cassandra.query import tuple_factory
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import lz4

cloud_config = {
    'secure_connect_bundle': '/path/to/secure-connect-dbname.zip'
}
auth_provider = PlainTextAuthProvider(username='user', password='pass')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


cluster = Cluster()
session = cluster.connect('mykeyspace')
profile = ExecutionProfile(
    load_balancing_policy=WhiteListRoundRobinPolicy(['127.0.0.1']),
    consistency_level=ConsistencyLevel.LOCAL_QUORUM,
    serial_consistency_level=ConsistencyLevel.LOCAL_SERIAL,
    request_timeout=15,
    row_factory=tuple_factory
)
cluster = Cluster(execution_profiles={EXEC_PROFILE_DEFAULT: profile})


print(session.execute("SELECT release_version FROM system.local").one())


rows = session.execute('SELECT name, age, email FROM users')
for user_row in rows:
    print(user_row.name, user_row.age, user_row.email)
