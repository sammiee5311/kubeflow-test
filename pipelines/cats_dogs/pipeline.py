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
    compiler.Compiler().compile(pipeline, __file__ + ".tar.gz")
