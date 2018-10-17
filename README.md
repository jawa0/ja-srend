# ja-srend
A convenient 3D software renderer with no dependencies. Well, some day. For now, it just outputs this test image:

![A test image rendered by ja-srend](./test-image.png "A sample image")

#### Running the Python version

    python test.py
    ./convert-test-image-to-png.sh

#### Building and running the C version (deprecated -- continuing in Python)

    make
    ./test-srend
    ./convert-test-image-to-png.sh

#### Viewing the generated image
On MacOS:

    open test-image.png
