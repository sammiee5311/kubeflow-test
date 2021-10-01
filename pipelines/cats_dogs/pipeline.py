import kfp.compiler as compiler
from kfp import dsl

@dsl.pipeline(
    name='sammiee-cats-dogs-2',
    description='sammiee cats dogs'
)

def pipeline():
    download_dataset = dsl.ContainerOp(
        name="download dataset",
        image="sammiee5311/download-dataset:lastest",
        arguments=[
            '--data_url', 'http://iguazio-sample-data.s3.amazonaws.com/catsndogs.zip',
            '--data_directory', './data'
            '--logger', 'log_url'
        ],
    )

    categorize_dataset = dsl.ContainerOp(
        name="categorize dataset",
        image="sammiee5311/categorize-dataset:lastest",
        arguments=[
            '--data_directory', './data'
            '--logger', 'log_url'
        ],
        file_outputs={
            'categories data' : './categories_data.json',
        }
    )

    categorize_dataset.after(download_dataset)

if __name__ == "__main__":
    compiler.Compiler().compile(pipeline, __file__ + ".tar.gz")