import os
# from resources.mongodb_crud import Data
from resources.firestore_crud import Data

import configuration
app = configuration.init()

configuration.api.add_resource(Data, '/data')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), threaded=True)
