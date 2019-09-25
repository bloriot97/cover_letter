# Cover Letter Generator

If you are sick of your `cover_letter_template.docx` file here is an alternative. 

## Dependencies 

The rendenring is done with [ReLaXed](https://github.com/RelaxedJS/ReLaXed) so make sure to install it :

```bash 
npm i -g relaxedjs
```



## Make a new cover letter

First you have to settup your personal information. Rename `info.json.example` and fill it in with valid information.

In the folder `cover_letters` create a folder for your cover letter.

Then you have to create 2 files 

- `info.json`: containes the local information for your cover letter.
- `content.md`: containes the main body of your cover letter.

The content of `info.json` should be as following: 

```json
{
  "company": {
    "name": "some name",
    "contact_name": "the name of the department",
    "address": "the address",
    "city": "the city"
  }
}
```

N.B. : you can set the date manually by adding a `date` field at the root of the json file.

Then you can build it:

```bash
python3 gen.py [the name of the folder]
```

**VOILÀAAA** 