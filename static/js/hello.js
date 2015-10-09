function Test($scope, $http) {
    $http.get('http://127.0.0.1:5000/update').
        success(function(data) {
            $scope.greeting = data;
        });
}
