# Used best practices

* Use `docker-compose` for easier managing of multi-container project
* Use `.dockerignore` to remove unnecessary files from build context
* Use multi-stage build to reduce size of final image
 (especialy for projects which involve compilation
 and produce unnecessary artifacts, e.g. `app_rust`)
* Install dependencies before copying source code,
 so that docker uses cache from previous build. Results in faster rebuild time.
* Minimize the number of layers, e.g. pack several commands in `RUN` instruction
* Use lightweight alpine images, especially for final stage of multi-stage build
* Avoid use of cache directory with pip when installing dependencies
* Use explicit version tags for images
* Sort multi-line arguments
* Avoid using root user to run the container
* Make executables not writable
