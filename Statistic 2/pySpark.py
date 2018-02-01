# 1 Check SparkContext
# Verify SparkContext
print(sc)
# <pyspark.context.SparkContext object at 0x7f0c53ea6ba8>

# Print Spark version
print(sc.version)
# 2.1.0

# SparkContext as your connection to the cluster
# SparkSession as your interface with that connection

# 2 Creating a SparkSession
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark =  SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
# <pyspark.sql.session.SparkSession object at 0x7f0c40ba7940>

# 3 Viewing tables
# Don't change this query
# query = "FROM flights SELECT * LIMIT 10"
query = "SELECT * FROM flights LIMIT 10"
# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()
#|year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|tailnum|flight|origin|dest|air_time|distance|hour|minute|
#|2014|   12|  8|     658|       -7|     935|       -5|     VX| N846VA|  1780|   SEA| LAX|     132|     954|   6|    58|

# 4 Put Spark to Pandas 
# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())
#  origin dest    N
#0    SEA  RNO    8
#1    SEA  DTW   98
#2    SEA  CLE    2
#3    SEA  LAX  450
#4    PDX  SEA  144

# 5 Put Pandas to Spark 
# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))
print(pd_temp.head(4))
#          0
#0  0.335689
#1  0.439782
#2  0.097781
# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(spark.catalog.listTables())
# DataFrame[0: double]

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")

# Examine the tables in the catalog again
print(spark.catalog.listTables())
# [Table(name='temp', database=None, description=None, tableType='TEMPORARY', isTemporary=True)]

# 6 Dropping the middle man

# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path,header=True)

# Show the data
airports.show()
#|faa|                name|             lat|              lon| alt| tz|dst|
#|04G|   Lansdowne Airport|      41.1304722|      -80.6195833|1044| -5|  A|

# 7 Creating columns

# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
print(flights.show())
# |year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|tailnum|flight|origin|dest|air_time|distance|hour|minute|
# |2014|   12|  8|     658|       -7|     935|       -5|     VX| N846VA|  1780|   SEA| LAX|     132|     954|   6|    58|
# Add duration_hrs
flights = flights.withColumn("duration_hrs",flights.air_time/60)

print(flights.show())
# |year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|tailnum|flight|origin|dest|air_time|distance|hour|minute|      duration_hrs|
# |2014|   12|  8|     658|       -7|     935|       -5|     VX| N846VA|  1780|   SEA| LAX|     132|     954|   6|    58|               2.2|

# 8 Filtering Data

# Filter flights with a SQL string
long_flights1 = flights.filter("distance > 1000")

# Filter flights with a boolean column
long_flights2 = flights.filter(flights.distance > 1000)

# Examine the data to check they're equal
print(flights.show())
print(long_flights1.show())
print(long_flights2.show())

# 9 Selecting
# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")

selected1.show()
# |tailnum|origin|dest|
# | N646SW|   PDX| DEN|
# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)
selected2.show()
# |tailnum|origin|dest|
# |   SEA| PDX|     OO|

# 10 Selecting II

# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)
speed1.show()
# |origin|dest|tailnum|         avg_speed|
# |   SEA| LAX| N846VA| 433.6363636363636|
# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
speed2.show()
# |origin|dest|tailnum|         avg_speed|
# |   SEA| LAX| N846VA| 433.6363636363636|

# 11 Aggregating
# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()
# |min(distance)|
# |          106|

# Find the longest flight from SEA in terms of duration
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()
# |max(air_time)|
# |          409|

# 12 Aggregating II
# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()
# |     avg(air_time)|
# |188.20689655172413|
# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()
# | sum(duration_hrs)|
# |25289.600000000126|

# 13 Grouping and Aggregating I
# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()
# |tailnum|count|
# | N442AS|   38|
# Group by origin
by_origin = flights.groupBy("origin")

# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()
# |origin|     avg(air_time)|
# |   SEA| 160.4361496051259|
# |   PDX|137.11543248288737|

# 14 Grouping and Aggregating II

# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")

# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()
# |month|dest|      avg(dep_delay)|
# |   11| TUS| -2.3333333333333335|
# Standard deviation
by_month_dest.agg(F.stddev("dep_delay")).show()
# |month|dest|stddev_samp(dep_delay)|
# |   11| TUS|    3.0550504633038935|

# 15 Join 1 
# Examine the data
print(airports.show())

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on="dest", how="leftouter")

# Examine the data again
print(flights_with_airports.show())

# 16 Join DataFrame
# Rename year column
planes = planes.withColumnRenamed('year','plane_year')

# Join the DataFrames
model_data = flights.join(planes, on='tailnum', how="leftouter")

model_data.show()
# |tailnum|year|month|day|dep_time|dep_delay|arr_time|arr_delay|carrier|flight|origin|dest|air_time|distance|hour|minute|plane_year|                type|  manufacturer|      model|engines|seats|speed|   engine|
# | N846VA|2014|   12|  8|     658|       -7|     935|       -5|     VX|  1780|   SEA| LAX|     132|     954|   6|    58|      2011|Fixed wing multi ...|        AIRBUS|   A320-214|      2|  182|   NA|Turbo-fan|

# 17 String to integer

# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))

# 17 Making Boolean
# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")

model_data.show()

# 18 Carrier
# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")

# 19 Destination 
# Create a StringIndexer
dest_indexer =  StringIndexer(inputCol="dest", outputCol="dest_index" )

# Create a OneHotEncoder
dest_encoder = OneHotEncoder(inputCol="dest_index",outputCol="dest_fact")

# 20 Assemble a vector

# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol='features')

# 21 Creae pipeline

# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])

# 22 Transform the data
# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)

# 23 Split the data
# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])

# 24 Create the modeler
# Import LogisticRegression
from pyspark.ml.classification import LogisticRegression

# Create a LogisticRegression Estimator
lr =  LogisticRegression()

# 25 Create the evaluator

# Import the evaluation submodule
import pyspark.ml.evaluation as evals

# Create a BinaryClassificationEvaluator
evaluator = evals.BinaryClassificationEvaluator( metricName="areaUnderROC")

# 26 Make a grid

# Import the tuning submodule
import pyspark.ml.tuning as tune

# Create the parameter grid
grid = tune.ParamGridBuilder()

# Add the hyperparameter
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
grid = grid.addGrid(lr.elasticNetParam, [0, 1])

# Build the grid
grid = grid.build()

# 27 Make the validator

# Create the CrossValidator
cv = tune.CrossValidator(estimator=lr,
                         estimatorParamMaps=grid,
                         evaluator=evaluator
                         )

# 28 Fit the model(s)
# Call lr.fit()
best_lr = lr.fit(training)

# Print best_lr
print(best_lr)

# 29 Evaluate the model
# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))




