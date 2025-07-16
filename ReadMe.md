
# Onion Bible API

The Onion Bible API is a Python/Flask-based API designed to power Bible apps and websites with features that are often hard to find elsewhere. It includes tools like Verse of the Day, fully formatted HTML Bible texts, and more — things that usually aren’t bundled together online.

While the API was originally built for use in my own Bible app, it’s available for others to use in their own projects as well.

It’s also open source, so if you see ways to improve it — whether that’s making things more efficient, fixing something, or adding new features — feel free to clone the repo and contribute.


## API Reference

#### Get The Verse Of The Day

```http
  https://obibleapi.onionservers.net/VerseOfTheDay/
```


#### Get A Bible Chapter

```http
  https://obibleapi.onionservers.net/<Version>/Chapters/<Chapter>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Version`      | `string` | **Required**. Different Bible Version. Ex: NIV, KJV, ESV |
| `Chapter`      | `string` | **Required**. Returns A Chapter Of The Bible. Ex: Genesis 1,  1 John 12 |

## Authors

- [@Onion2243](https://github.com/Onion2243)


## License

[CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)

PS: By NonCommerical 