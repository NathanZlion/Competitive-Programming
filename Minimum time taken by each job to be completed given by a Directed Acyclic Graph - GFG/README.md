# Minimum time taken by each job to be completed given by a Directed Acyclic Graph
## Medium
<div class="problems_problem_content__Xm_eO"><p><span style="font-size:18px">Given a&nbsp;<strong>Directed Acyclic Graph</strong>&nbsp;having&nbsp;<strong>V&nbsp;</strong>vertices and<strong>&nbsp;E&nbsp;</strong>edges, where each edge&nbsp;<strong>{U, V}</strong>&nbsp;represents the Jobs&nbsp;<strong>U</strong>&nbsp;and&nbsp;<strong>V</strong>&nbsp;such that Job&nbsp;<strong>V</strong>&nbsp;can only be started only after completion of Job&nbsp;<strong>U</strong>. The task is to determine the minimum time taken by each job to be completed where each Job takes unit time to get completed.</span></p>

<p><strong><span style="font-size:18px">Example 1:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=10
M=13
edges[]={{1,3},{1,4},{1,5},{2,3},{2,8},{2,9},{3,6},{4,6},{4,8},{5,8},{6,7},{7,8},{8,10}}
<strong>Output:</strong>
time[]={1,1,2,2,2,3,4,5,2,6 }
<strong>Explanation:</strong>
Start jobs 1 and 2 at the beginning and complete them at 1 unit of time. 
Since, all the jobs on which need to be completed before the jobs 3, 4, 5, and 9 are completed. So, we can start these jobs at 1st unit of time and complete these at 2nd unit of time after the completion of the dependent Job.
Similarly, 
Job 6 can only be done after the 3rd and 4th jobs are done. So, start it at the 2nd unit of time and complete it at the 3rd unit of time.
Job 7 can only be done after job 6 is done. So, you can start it at the 3rd unit of time and complete it at the 4th unit of time.
Job 8 can only be done after the 4th, 5th, and 7th jobs are done. So, start it at the 4th unit of time and complete it at the 5th unit of time.
Job 10 can only be done after the 8th job is done. So, start it at the 5th unit of time and complete it at the 6th unit of time.</span></pre>

<p><strong><span style="font-size:18px">Example2:</span></strong></p>

<pre><span style="font-size:18px"><strong>Input:</strong>
N=7
M=7
edges[]={{1,2},{2,3},{2,4},{2,5},{3,6},{4,6},{5,7}}
<strong>Output:</strong>
time[]={1,2,3,3,3,4,4}
<strong>Explanation:</strong>
Start Job 1 at the beginning and complete it at 1st unit of time.
Job 2 can only be done after 1st Job is done. So, start it at 1st unit of time and complete it at 2nd unit of time.
Since, Job 3, 4, and 5 have the only dependency on the 2nd Job. So, start these jobs at the 2nd unit of time and complete these at the 3rd unit of time.
Job 6 can only be done after the 3rd and 4th Job is done. So, start it at the 3rd unit of time and complete it at the 4th unit of time.
Job 7 can only be done after the 5th Job is done. So, start it at the 3rd hour and complete it at the 4th unit of time.</span></pre>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Your Task:</strong><br>
You don't need to read input or print anything. Your task is to complete the function <strong>minimumTime()</strong>&nbsp;which takes the edge list e[] of the graph, its size number of nodes N<strong>&nbsp;</strong>and M the number of edges as input parameters and returns the time array.</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Expected Time Complexity:</strong>&nbsp;<em>O(V+E), where V is the number of nodes and E is the number of edges.&nbsp;</em><br>
<strong>Expected Auxiliary Space:</strong>&nbsp;O(V)</span></p>

<p>&nbsp;</p>

<p><span style="font-size:18px"><strong>Constraints:</strong><br>
1 &lt;= N &lt;= 10</span><sup><span style="font-size:15px">3</span></sup><br>
<span style="font-size:18px">1&lt;=M&lt;=N*(N-1)/2</span><br>
<span style="font-size:18px">1&lt;=edges[i][0],edges[i][1]&lt;=N.</span></p>
</div>