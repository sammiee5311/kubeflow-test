import os
import kfp.compiler as compiler
from kfp import dsl, Client


def print_op(msg):
    return dsl.ContainerOp(
        name='Print',
        image='python',
        command=['echo', msg],
)

@dsl.pipeline(
    name='sammiee-iris-2',
    description='sammiee iris test 2'
)


def pipeline_iris():
    add_p = dsl.ContainerOp(
        name="load iris data pipeline",
        image="sammiee5311/iris-data-load:latest",
        arguments=[
            '--data_path', './Iris.csv'
        ],
        file_outputs={'iris' : '/iris.csv'}
    )

    train_and_eval = dsl.ContainerOp(
        name="training pipeline",
        image="sammiee5311/iris-model-train:latest",
        arguments=[
            '--data', add_p.outputs['iris']
        ],
        file_outputs={
            'accuracy' : '/accuracy.json',
            'mlpipeline-metrics' : '/mlpipeline-metrics.json'
        }
    )

    train_and_eval.after(add_p)
    baseline = 0.7

    with dsl.Condition(train_and_eval.outputs['accuracy'] > baseline):
        print_op(f"Your accuracy is higher than baseline accuracy: {train_and_eval.outputs['accuracy']}")
    
    with dsl.Condition(train_and_eval.outputs['accuracy'] < baseline):
        print_op(f"Your accuracy is lower than baseline accuracy: {train_and_eval.outputs['accuracy']}")


if __name__ == "__main__":
    host = os.environ['URI']
    cookies = os.environ['COOKIES']
    namespace = os.environ['NAMESPACE']

    pipeline_name = "sammiee-iris-2"
    pipeline_file = f'{pipeline_name}.tar.gz'

    experiment_name = 'iris-experiment-1'
    run_name = 'iris-run'

    # client = Client(host=host, namespace=namespace, cookies=cookies)

    # compiler.Compiler().compile(pipeline_iris, pipeline_file)

    # pipeline = client.upload_pipeline(
    #     pipeline_package_path=pipeline_file,
    #     pipeline_name=pipeline_name
    # )

    # experiment = client.create_experiment(name=experiment_name, namespace=namespace)
    # run = client.run_pipeline(experiment.id, run_name, pipeline_id=pipeline.id)
