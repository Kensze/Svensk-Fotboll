var app = angular.module('myApp', ['ngSanitize'])

.filter('toTrusted', ['$sce', function($sce) {
    return function(text) {
        return $sce.trustAsHtml(text);
    };
}])

app.controller('myController', ['$scope', '$http','$location', '$window', '$sce',  function($scope, $http, $location, $window, $sce, $filter, $compile) {


    $scope.imdbID = function() {
        var pathname = $window.location.pathname.substring(1);
        var parts = pathname.split(/\//);
        if (parts.length > 1 ) {
            $scope.ID = parts[1];
        }
        $http.get('/movies/' + $scope.ID).success(function(data) {
            $scope.greeting = data;
    });
    }

    $scope.imdbTrailer = function() {
        var pathname = $window.location.pathname.substring(1);
        var parts = pathname.split(/\//);
        if (parts.length > 1 ) {
            $scope.ID = parts[1];
        }
       $http.get('/trailers/' + $scope.ID).success(function(data) {
        $scope.trailer = data;
    });
    }

    $scope.clickButton = function() {
        $http.get('/search').success(function(data) {
            $scope.greeting = data;
    });
    }

    $scope.doSearch = function(query){
        $http({
            url: 'search',
            method: "POST",
            data: {search: query},
        }).success(function(data) {
            $scope.greeting = data;
        });
    }

    }]);
