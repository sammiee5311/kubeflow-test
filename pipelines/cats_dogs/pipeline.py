import os
import kfp.compiler as compiler
from kfp import dsl


@dsl.pipeline(name="sammiee-cats-dogs-2", description="sammiee cats dogs")
def pipeline():
    download_dataset = dsl.ContainerOp(
        name="download dataset",
        image="sammiee5311/download-dataset:latest",
        arguments=[
            "--data_url",
            "http://iguazio-sample-data.s3.amazonaws.com/catsndogs.zip",
            "--data_directory",
            "./data",
        ],
    )

    categorize_dataset = dsl.ContainerOp(
        name="categorize dataset",
        image="sammiee5311/categorize-dataset:latest",
        arguments=["--data_directory", "./data"],
        file_outputs={
            "categories data": "/categories_data.json",
        },
    )

    categorize_dataset.after(download_dataset)


if __name__ == "__main__":
    host = os.environ["URI"]
    cookies = os.environ["COOKIES"]
    namespace = os.environ["NAMESPACE"]

    pipeline_name = "sammiee-cats-dogs"
    pipeline_file = f"{pipeline_name}.tar.gz"

    experiment_name = "cats-dogs-experiment"
    run_name = "cats-dogs-run"

    compiler.Compiler().compile(pipeline, __file__ + ".tar.gz")

    # client = Client(host=host, namespace=namespace, cookies=cookies)

    # pipeline = client.upload_pipeline(
    #     pipeline_package_path=pipeline_file,
    #     pipeline_name=pipeline_name
    # )

    # experiment = client.create_experiment(name=experiment_name, namespace=namespace)
    # run = client.run_pipeline(experiment.id, run_name, pipeline_id=pipeline.id)

