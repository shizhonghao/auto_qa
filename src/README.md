# Set up

* ~~Here we used virtual environment on the project, you may install it using `pip install virtualenv`

* ~~After installation cd to `src\env` directory and enter `Scripts\activate` to activate virtual environment

* ~~To exit, use `deactivate` 

* ~~How to use virtualenv ([link](http://blog.51cto.com/qicheng0211/1561685))

* We use word2vec in `gensim`. How to install([link](https://radimrehurek.com/gensim/install.html))

* For Chinese word segmentation we use `jieba` ([link](https://github.com/fxsjy/jieba))

## back_end

* flask is used to build the back_end of this project, run `src/back_end/run.py` to init back_end service on localhost:5000

* route `/` is the query page, the query should be a GET request with the form `/query?question=xxxxxx`, the backend then returns a json with the following format:

```json
{
  answer:[
    {
      answer : "str",
      percentage : "int"([0,100])
    },
    {
      answer : "str",
      percentage : "int"([0,100])
    },
    ...
  ]
  cnt : "int" `number of answers`
}
```

## front_end

* use `npm run dev` under `src/front_end` to init front_end hot-reload dev 

## word2vec

* 
