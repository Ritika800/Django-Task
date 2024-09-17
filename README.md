# Django-Task

## Question 1:- By default, are Django signals executed synchronously or asynchronously? 
Ans:-  By default, Django signal are executed synchronously. This means that When a signal is triggered, the associated receivers (the functions that are called in response to the signal) are executed synchronously, meaning that each receiver must complete before the next one can begin..
When using synchronous signal handling, the application must wait for all the receivers to complete before continuing with other requests. This can cause performance issues if you have many signals or long-running signal handlers.
In conclusion, Django signals are not inherently asynchronous.
 Code snippet is attached name is sync.py

## Question:-  Do Django signals run in the same thread as the caller?
Ans:- Yes , Django signals run in the same thread  as the process that triggers them. This means that when a Django signal is emitted, it is handled synchronously within the same thread where the signal was sent. If a signal handler takes time to process (e.g., performing a time-consuming task like sending an email or processing large data), the main thread that emitted the signal will wait until the signal handler finishes executing.
However, Django signals can be configured to run asynchronously to prevent the main process from waiting for the signal to complete. Running signals asynchronously is beneficial for performance optimization in cases where the signal handler performs heavy tasks, and you want to offload them to a separate worker or thread.
Code snippet is attached name is signals.py

## Question 3: By default, do Django signals run in the same database transaction as the caller?
Ans:- Yes, by default, Django signals run in the same database transaction as the caller, especially when the signal is tied to a model action (e.g., post_save or pre_save). If the transaction is rolled back, any changes made by the signal will also be rolled back.
Code snippet is attached name is database.py

