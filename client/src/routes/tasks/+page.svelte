<script>
   let tasks = []
   let list_output = ''
   let final_word_arr = []

   const event_tasks = (e) => {
         // pull data from user input 
         tasks.push(e.target.value)
   }

   const addtasks = (e) => {
      // this function should add tasks to the list dynamically 
      list_output = tasks.pop()
      final_word_arr.push(list_output)
      console.log(final_word_arr)
   }

</script>

<!-- user can input new tasks for the specified date
users can add, update and delete tasks from the list as well from the back-end
when users type something the data gets stored and when the on click is fired the user adds a tasks one by one -->


<main>
   {#each final_word_arr as final_word_arrs}
     <li>{final_word_arrs}</li>
   {/each}
   <div>
      <div>Dummy Calendar data here</div>
      <h2>Tasks in relevance to the Calendar</h2>
   </div>
   <span><input on:input={event_tasks}/>Today's Task</span>
   <br/>
<button on:click={addtasks}>Add Tasks</button>
</main>

<style>


</style>