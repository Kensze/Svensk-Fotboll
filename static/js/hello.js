var app = angular.module('myApp', []);

app.controller('myController', ['$scope', '$http', function($scope, $http) {

    $scope.clickButton = function() {
        $http.get('http://127.0.0.1:5000/update').success(function(data) {
            $scope.greeting = data;
    });
    }

    $scope.doSearch = function(query){
        $http({
            url: 'update',
            method: "POST",
            data: {search: query},
           //data: {search: query},
            //data: JSON.stringify(query)
        }).success(function(data) {
            $scope.greeting = data;
        });
    }


}]);
