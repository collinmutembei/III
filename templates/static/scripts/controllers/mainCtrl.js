angular.module('blstApp').controller("MainController", function($scope, MainService){
    $scope.bucketlists = MainService.bucketlists.getBucketlists();

    $scope.$on('updateBucketlist', function () {
        $scope.bucketlists = MainService.bucketlists.getBucketlists();
    });
    $scope.add_bucketlist = function(){
        bucketlist = {
            name: $scope.bucketlist.name
        }
        MainService.bucketlists.addBucketlist(bucketlist).
        $promise.
        then(function(result){
            $scope.add_bucketlist_message = "bucketlist created"
            $scope.$emit('updateBucketlist');
            $scope.bucketlist = {}
        }).
        catch(function(response){
            $scope.add_bucketlist_message = "bucketlist not created"
            console.log($scope.bucketlist)
        })
    }
});
