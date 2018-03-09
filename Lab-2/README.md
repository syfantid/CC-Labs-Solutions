## Cloud Computing Lab II

### Task 2.1.1: Word Count 1
This task solely handles simple text tokenization and does not deal with stop words or punctuation elimination.

#### Console Output - 10 Most Common Words
[('the', 1343), (',', 1251), ('.', 810), (')', 638), ('(', 637), ('of', 586), ('to', 491), ('a', 468), (':', 454), ('in', 417)]

#### Console Output - Word Count
25151

### Task 2.1.2: Remove Punctuation
This task solely handles simple text tokenization and punctuation removal and does not deal with stop words.

#### Console Output - 10 Most Common Words
[('the', 1444), ('of', 586), ('to', 531), ('in', 506), ('a', 481), ('and', 346), ('is', 289), ('we', 279), ('that', 275), ('this', 268)]

#### Console Output - Word Count
19593

### Task 2.1.3: Stopwords
This task solely handles simple text tokenization and punctuation removal and does not deal with stop words.

#### Console Output - 10 Most Common Words
[('tensorflow', 193), ('data', 102), ('tensor', 99), ('code', 90), ('learning', 81), ('function', 74), ('one', 73), ('use', 65), ('example', 64), ('available', 63)]

#### Console Output - Word Count
11220

### Task 2.2.1: Accessing your Twitter Account Information
The output of this task is given below:

Name: ozgekoroglu  
Location: Barcelona, Spain  
Friends: 166  
Created: 2010-02-15 16:22:13  
Description: ITU Mathematics Engineering koalasevensarılgantiplerdenim  

### Task 2.2.2: Accessing Tweets

#### Home Timeline

```json
{
  "in_reply_to_user_id_str": null,
  "retweet_count": 15,
  "text": "de baby boomers found that the average IQ score of a blonde is actually higher than those with other hair colors.A study of naturally blon",
  "retweeted": false,
  "in_reply_to_screen_name": null,
  "is_quote_status": false,
  "user": {
    "profile_link_color": "0D9BA8",
    "friends_count": 1,
    "protected": false,
    "is_translator": false,
    "lang": "en",
    "profile_sidebar_fill_color": "FFFFFF",
    "notifications": false,
    "contributors_enabled": false,
    "has_extended_profile": false,
    "id_str": "95023423",
    "statuses_count": 151824,
    "listed_count": 18368,
    "profile_background_tile": false,
    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/458303470945058816/1IXg4LCd.jpeg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/95023423/1464904901",
    "default_profile_image": false,
    "created_at": "Sun Dec 06 16:07:01 +0000 2009",
    "profile_background_color": "C0DEED",
    "name": "UberFacts",
    "profile_text_color": "000000",
    "following": true,
    "id": 95023423,
    "utc_offset": -21600,
    "followers_count": 14517656,
    "default_profile": false,
    "profile_sidebar_border_color": "000000",
    "is_translation_enabled": true,
    "screen_name": "UberFacts",
    "entities": {
      "description": {
        "urls": []
      },
      "url": {
        "urls": [
          {
            "expanded_url": "https://amzn.com/0062441167",
            "indices": [
              0,
              23
            ],
            "url": "https://t.co/SZLgCWyHWM",
            "display_url": "amzn.com/0062441167"
          }
        ]
      }
    },
    "description": "The most unimportant things you'll never need to know.",
    "time_zone": "Central Time (US & Canada)",
    "follow_request_sent": false,
    "favourites_count": 1080,
    "url": "https://t.co/SZLgCWyHWM",
    "verified": true,
    "profile_image_url": "http://pbs.twimg.com/profile_images/615696617165885440/JDbUuo9H_normal.jpg",
    "translator_type": "regular",
    "geo_enabled": false,
    "profile_use_background_image": true,
    "location": "Worldwide! ",
    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/458303470945058816/1IXg4LCd.jpeg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/615696617165885440/JDbUuo9H_normal.jpg"
  },
  "in_reply_to_status_id": null,
  "source": "<a href=\"http://bufferapp.com\" rel=\"nofollow\">Buffer</a>",
  "in_reply_to_status_id_str": null,
  "created_at": "Fri Mar 09 08:47:00 +0000 2018",
  "coordinates": null,
  "favorited": false,
  "favorite_count": 63,
  "id": 972030984311930881,
  "lang": "en",
  "id_str": "972030984311930881",
  "entities": {
    "user_mentions": [],
    "urls": [],
    "symbols": [],
    "hashtags": []
  },
  "geo": null,
  "truncated": false,
  "place": null,
  "in_reply_to_user_id": null,
  "contributors": null
}
```

#### Friend list

```json
{
  "profile_link_color": "1DA1F2",
  "listed_count": 0,
  "protected": false,
  "profile_sidebar_fill_color": "DDEEF6",
  "blocking": false,
  "contributors_enabled": false,
  "id_str": "951810826805153794",
  "statuses_count": 45,
  "live_following": false,
  "profile_banner_url": "https://pbs.twimg.com/profile_banners/951810826805153794/1515865828",
  "created_at": "Fri Jan 12 13:39:19 +0000 2018",
  "name": "eliftubaok",
  "is_translation_enabled": false,
  "id": 951810826805153794,
  "lang": "tr",
  "profile_background_tile": false,
  "screen_name": "eliftubaok",
  "time_zone": null,
  "favourites_count": 68,
  "url": null,
  "notifications": false,
  "translator_type": "none",
  "profile_use_background_image": true,
  "profile_background_color": "F5F8FA",
  "friends_count": 118,
  "is_translator": false,
  "has_extended_profile": true,
  "default_profile": true,
  "description": "Coffeeaddict.\nMusiclover.\nAlmostfoodie.",
  "muting": false,
  "profile_background_image_url_https": null,
  "location": "",
  "blocked_by": false,
  "profile_text_color": "333333",
  "following": true,
  "utc_offset": null,
  "followers_count": 34,
  "profile_sidebar_border_color": "C0DEED",
  "status": {
    "in_reply_to_user_id_str": null,
    "retweet_count": 0,
    "text": "Ayn\u0131 vapurdan indi\u011fin halde dolmu\u015f s\u0131ras\u0131na senden \u00f6nce ge\u00e7enlerden nefret edenlerdenim",
    "retweeted": false,
    "in_reply_to_screen_name": null,
    "is_quote_status": false,
    "id_str": "966186975475757062",
    "in_reply_to_status_id": null,
    "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
    "in_reply_to_status_id_str": null,
    "created_at": "Wed Feb 21 05:45:00 +0000 2018",
    "coordinates": null,
    "favorited": false,
    "favorite_count": 0,
    "id": 966186975475757062,
    "lang": "tr",
    "entities": {
      "user_mentions": [],
      "urls": [],
      "symbols": [],
      "hashtags": []
    },
    "geo": null,
    "truncated": false,
    "place": null,
    "in_reply_to_user_id": null,
    "contributors": null
  },
  "entities": {
    "description": {
      "urls": []
    }
  },
  "default_profile_image": false,
  "follow_request_sent": false,
  "verified": false,
  "profile_image_url": "http://pbs.twimg.com/profile_images/951812515335467008/2Cf6U9X1_normal.jpg",
  "geo_enabled": true,
  "profile_background_image_url": null,
  "profile_image_url_https": "https://pbs.twimg.com/profile_images/951812515335467008/2Cf6U9X1_normal.jpg"
}
```

<details> 
<summary>#### User List</summary>

```json
{
  "in_reply_to_user_id_str": null,
  "retweet_count": 713,
  "text": "RT @ozgurugzo: +after all this time?\n-always. https://t.co/mRmQlBAGSx",
  "retweeted": true,
  "in_reply_to_screen_name": null,
  "is_quote_status": false,
  "extended_entities": {
    "media": [
      {
        "source_status_id_str": "818535595765104640",
        "id": 818535574491582464,
        "type": "photo",
        "media_url": "http://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
        "source_status_id": 818535595765104640,
        "indices": [
          46,
          69
        ],
        "display_url": "pic.twitter.com/mRmQlBAGSx",
        "source_user_id": 43098432,
        "id_str": "818535574491582464",
        "source_user_id_str": "43098432",
        "url": "https://t.co/mRmQlBAGSx",
        "media_url_https": "https://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
        "expanded_url": "https://twitter.com/ozgurugzo/status/818535595765104640/photo/1",
        "sizes": {
          "medium": {
            "resize": "fit",
            "w": 736,
            "h": 905
          },
          "small": {
            "resize": "fit",
            "w": 553,
            "h": 680
          },
          "large": {
            "resize": "fit",
            "w": 736,
            "h": 905
          },
          "thumb": {
            "resize": "crop",
            "w": 150,
            "h": 150
          }
        }
      }
    ]
  },
  "user": {
    "profile_link_color": "B3454B",
    "friends_count": 112,
    "protected": true,
    "is_translator": false,
    "lang": "en",
    "profile_sidebar_fill_color": "212121",
    "notifications": false,
    "contributors_enabled": false,
    "has_extended_profile": true,
    "id_str": "114496555",
    "statuses_count": 1521,
    "listed_count": 1,
    "profile_background_tile": true,
    "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/252257819/Leighton-Meester_1.jpg_e_18a371e83b1bde810f899df57848670ch.jpg",
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/114496555/1405958150",
    "default_profile_image": false,
    "created_at": "Mon Feb 15 16:22:13 +0000 2010",
    "profile_background_color": "6B6161",
    "name": "ozgekoroglu",
    "profile_text_color": "A85959",
    "following": false,
    "id": 114496555,
    "utc_offset": -10800,
    "followers_count": 166,
    "default_profile": false,
    "profile_sidebar_border_color": "505959",
    "is_translation_enabled": false,
    "screen_name": "ozgeekoroglu",
    "entities": {
      "description": {
        "urls": []
      }
    },
    "description": "ITU Mathematics Engineering koalasevensar\u0131lgantiplerdenim",
    "time_zone": "Greenland",
    "follow_request_sent": false,
    "favourites_count": 1788,
    "url": null,
    "verified": false,
    "profile_image_url": "http://pbs.twimg.com/profile_images/793024436307894272/jqZwq6wW_normal.jpg",
    "translator_type": "none",
    "geo_enabled": true,
    "profile_use_background_image": true,
    "location": "Barcelona, Espa\u00f1a",
    "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/252257819/Leighton-Meester_1.jpg_e_18a371e83b1bde810f899df57848670ch.jpg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/793024436307894272/jqZwq6wW_normal.jpg"
  },
  "retweeted_status": {
    "in_reply_to_user_id_str": null,
    "retweet_count": 713,
    "text": "+after all this time?\n-always. https://t.co/mRmQlBAGSx",
    "retweeted": true,
    "in_reply_to_screen_name": null,
    "is_quote_status": false,
    "extended_entities": {
      "media": [
        {
          "id_str": "818535574491582464",
          "type": "photo",
          "url": "https://t.co/mRmQlBAGSx",
          "id": 818535574491582464,
          "media_url_https": "https://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
          "display_url": "pic.twitter.com/mRmQlBAGSx",
          "media_url": "http://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
          "expanded_url": "https://twitter.com/ozgurugzo/status/818535595765104640/photo/1",
          "indices": [
            31,
            54
          ],
          "sizes": {
            "medium": {
              "resize": "fit",
              "w": 736,
              "h": 905
            },
            "small": {
              "resize": "fit",
              "w": 553,
              "h": 680
            },
            "large": {
              "resize": "fit",
              "w": 736,
              "h": 905
            },
            "thumb": {
              "resize": "crop",
              "w": 150,
              "h": 150
            }
          }
        }
      ]
    },
    "user": {
      "profile_link_color": "1B95E0",
      "friends_count": 366,
      "protected": false,
      "is_translator": false,
      "lang": "tr",
      "profile_sidebar_fill_color": "FFFFFF",
      "notifications": false,
      "contributors_enabled": false,
      "has_extended_profile": false,
      "id_str": "43098432",
      "statuses_count": 13072,
      "listed_count": 601,
      "profile_background_tile": true,
      "profile_background_image_url_https": "https://pbs.twimg.com/profile_background_images/663468149661044736/D_o0CQT1.png",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/43098432/1519393535",
      "default_profile_image": false,
      "created_at": "Thu May 28 12:23:12 +0000 2009",
      "profile_background_color": "000000",
      "name": "ozgurugzo",
      "profile_text_color": "5F6396",
      "following": false,
      "id": 43098432,
      "utc_offset": -10800,
      "followers_count": 186470,
      "default_profile": false,
      "profile_sidebar_border_color": "000000",
      "is_translation_enabled": true,
      "screen_name": "ozgurugzo",
      "entities": {
        "description": {
          "urls": []
        }
      },
      "description": "bay\u0131l\u0131yorum kendime can\u0131m kendim",
      "time_zone": "Greenland",
      "follow_request_sent": false,
      "favourites_count": 10934,
      "url": null,
      "verified": false,
      "profile_image_url": "http://pbs.twimg.com/profile_images/723833814355705856/K84isY8d_normal.jpg",
      "translator_type": "regular",
      "geo_enabled": false,
      "profile_use_background_image": true,
      "location": "iamozgurugzo@gmail.com",
      "profile_background_image_url": "http://pbs.twimg.com/profile_background_images/663468149661044736/D_o0CQT1.png",
      "profile_image_url_https": "https://pbs.twimg.com/profile_images/723833814355705856/K84isY8d_normal.jpg"
    },
    "in_reply_to_status_id": null,
    "source": "<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>",
    "in_reply_to_status_id_str": null,
    "created_at": "Mon Jan 09 19:11:08 +0000 2017",
    "coordinates": null,
    "favorited": true,
    "favorite_count": 2696,
    "id": 818535595765104640,
    "lang": "en",
    "id_str": "818535595765104640",
    "entities": {
      "user_mentions": [],
      "urls": [],
      "media": [
        {
          "id_str": "818535574491582464",
          "type": "photo",
          "url": "https://t.co/mRmQlBAGSx",
          "id": 818535574491582464,
          "media_url_https": "https://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
          "display_url": "pic.twitter.com/mRmQlBAGSx",
          "media_url": "http://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
          "expanded_url": "https://twitter.com/ozgurugzo/status/818535595765104640/photo/1",
          "indices": [
            31,
            54
          ],
          "sizes": {
            "medium": {
              "resize": "fit",
              "w": 736,
              "h": 905
            },
            "small": {
              "resize": "fit",
              "w": 553,
              "h": 680
            },
            "large": {
              "resize": "fit",
              "w": 736,
              "h": 905
            },
            "thumb": {
              "resize": "crop",
              "w": 150,
              "h": 150
            }
          }
        }
      ],
      "symbols": [],
      "hashtags": []
    },
    "geo": null,
    "truncated": false,
    "place": null,
    "in_reply_to_user_id": null,
    "contributors": null,
    "possibly_sensitive": false
  },
  "in_reply_to_status_id": null,
  "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
  "in_reply_to_status_id_str": null,
  "created_at": "Sat Oct 28 21:16:43 +0000 2017",
  "coordinates": null,
  "favorited": true,
  "favorite_count": 0,
  "id": 924384455300698113,
  "lang": "en",
  "id_str": "924384455300698113",
  "entities": {
    "user_mentions": [
      {
        "name": "ozgurugzo",
        "id_str": "43098432",
        "indices": [
          3,
          13
        ],
        "screen_name": "ozgurugzo",
        "id": 43098432
      }
    ],
    "urls": [],
    "media": [
      {
        "source_status_id_str": "818535595765104640",
        "id": 818535574491582464,
        "type": "photo",
        "media_url": "http://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
        "source_status_id": 818535595765104640,
        "indices": [
          46,
          69
        ],
        "display_url": "pic.twitter.com/mRmQlBAGSx",
        "source_user_id": 43098432,
        "id_str": "818535574491582464",
        "source_user_id_str": "43098432",
        "url": "https://t.co/mRmQlBAGSx",
        "media_url_https": "https://pbs.twimg.com/media/C1wFxKmXUAAgsKU.jpg",
        "expanded_url": "https://twitter.com/ozgurugzo/status/818535595765104640/photo/1",
        "sizes": {
          "medium": {
            "resize": "fit",
            "w": 736,
            "h": 905
          },
          "small": {
            "resize": "fit",
            "w": 553,
            "h": 680
          },
          "large": {
            "resize": "fit",
            "w": 736,
            "h": 905
          },
          "thumb": {
            "resize": "crop",
            "w": 150,
            "h": 150
          }
        }
      }
    ],
    "symbols": [],
    "hashtags": []
  },
  "geo": null,
  "truncated": false,
  "place": null,
  "in_reply_to_user_id": null,
  "contributors": null,
  "possibly_sensitive": false
}
```
</details>

