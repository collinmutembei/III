angular.module('blstApp').controller("MainController", function($scope, MainService){
    $scope.bucketlists = MainService.bucketlists.getBucketlists();
});
