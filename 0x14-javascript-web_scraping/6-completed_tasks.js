#!/usr/bin/node

const requests = require('request');

const taskCompleted = (url) => {
	requests.get(url, (error, response, body) => {
		if (error){
			console.error(error);
		}
		else {
			const todos = JSON.parse(body);
			const tasksByUser = {};
		
			todos.forEach(todo => {
				if (todo.completed) {
					if (tasksByUser[todo.userId]) {
						tasksByUser[todo.userId]++;
					} else {
						tasksByUser[todo.userId] = 1;
					}
				}
			});

			console.log(tasksByUser);
		}
	});
}

const url = process.argv[2];
taskCompleted(url);
