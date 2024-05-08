# todo : declare proper _mytyping types 
# from _mytyping import Int, MatrixLike, ArrayLike, Float

# todo : insert weight field 

class myKNeighborRegression():
    def __init__(self,
                 #n_neighbors : Int = 5,
                 n_neighbors = 5,
                 *,
                 weight : None,
                 #p : Int = 2,
                 p = 2,
                 metrics = "minkowski",
                 metrics_params : None | dict = None,
                 ) -> None:
        self._n_neighbors = n_neighbors
        self._p = p
        self._weight = weight
        self._metrics = metrics
        self._metrics_params = metrics_params

        pass

    def fit(
            self,

            
            ):
        pass

    def predict(self):
        pass

    def score(self):
        pass