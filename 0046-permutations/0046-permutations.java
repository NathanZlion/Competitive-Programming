class Solution {
    ArrayList<int[]> all_permutations = new ArrayList<> ();
    
    public List<List<Integer>> permute(int[] nums) {
        ArrayList<Integer> built = new ArrayList<Integer>();
        backTrack(built, nums);

        List<List<Integer>> listOfLists = new ArrayList<>();

        for (int[] arr : all_permutations) {
            List<Integer> list = Arrays.asList(Arrays.stream(arr).boxed().toArray(Integer[]::new));
            listOfLists.add(list);
        }
        return listOfLists;
    }

    public static int[] removeAtIndex(int index, int[] array){

    if (index >= array.length){
          int[] empty_array = new int[0];
            return empty_array;
    }
        
      int[] firstHalf = Arrays.copyOfRange(array, 0, index);
      int[] secondHalf = Arrays.copyOfRange(array, index+1, array.length);
      int[] newArr = new int[firstHalf.length + secondHalf.length];
      
      for (int i =0; i < firstHalf.length; i++){
          newArr[i] = firstHalf[i];
      }
      
      for (int j = 0; j < secondHalf.length; j++){
          newArr[j + firstHalf.length] =secondHalf[j];
      }

      return newArr;
    }

    public void backTrack(ArrayList<Integer> built, int[] available){
        
        if (available.length == 0){

            int[] arr = new int[built.size()];
            for (int i = 0; i < built.size(); i++) {
                arr[i] = built.get(i);
            }
            all_permutations.add(arr);

            return ;
        }
        
        for (int index = 0; index < available.length; index++){
            built.add(built.size(), available[index]);
            backTrack(built, removeAtIndex(index, available));
            built.remove(built.size()-1);
        }
    }
}
