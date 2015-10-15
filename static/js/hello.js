var app = angular.module('myApp', []);

app.controller('myController', ['$scope', '$http','$location', '$window', function($scope, $http, $location, $window) {

    $scope.to_trusted = function(html_code) {
            return $sce.trustAsHtml(html_code);
    }

    $scope.imdbID = function() {
        //$scope.ID = $location.pathname();
        //$scope.ID = $window.location.pathname;

        var pathname = $window.location.pathname.substring(1);
        var parts = pathname.split(/\//);
        if (parts.length > 1 ) {
                 $scope.ID = parts[1];
        }
        console.log($scope.ID);

        //$scope.ID = "asd";
        $http.get('http://127.0.0.1:5000/movies/' + $scope.ID).success(function(data) {
            $scope.greeting = data;
            });
    }



    $scope.imdbTrailer = function() {
        //$scope.ID = $location.pathname();
        //$scope.ID = $window.location.pathname;

        var pathname = $window.location.pathname.substring(1);
        var parts = pathname.split(/\//);
        if (parts.length > 1 ) {
                 $scope.ID = parts[1];
        }
        console.log($scope.ID);

        //$scope.ID = "asd";
        $http.get('http://www.myapifilms.com/taapi?imdb=tt0468569&count=1&format=JSON').success(function(data) {
        //$http.get('http://127.0.0.1:5000/movies/' + $scope.ID).success(function(data) {
            $scope.trailer = data;
            });
    }



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
        }).success(function(data) {
            $scope.greeting = data;
        });
    }

    $scope.doTrailer = function(query){
        $http({
            url: 'trailer',
            method: "POST",
            data: {search: query},
        }).success(function(data) {
            $scope.trailers = data;
        });
    }



}]);
