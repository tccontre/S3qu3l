pattern = \
{
"sql_injectio_rule01": "[\'|\"][\s|\&|\^|\*][\'|\"]",
"sql_injectio_rule02": "\'\s(?i)or\s1\=1\slimit\s1\s\-\-\s\-\+",
"sql_injectio_rule03": "\'\=\"(?i)or\'",
"sql_injectio_rule04": "\'\s(?i)or\s\'\'[\-|\s|&|\^|\*]\'",
"sql_injectio_rule05": "[\'|\"]\-\|\|0[\'|\"]",
"sql_injectio_rule06": "[\'|\"]\-\|\|0[\'|\"]",
"sql_injectio_rule07": "[\'|\"][\s|\&|\^|\*][\'|\"]",
"sql_injectio_rule08": "\"\s(?i)or\s\"\"[\-|\s|\&|\^|\*|]\"",
"sql_injectio_rule09": "\"\s(?i)or\s\"\"[\-|\s|\&|\^|\*|]\"",
"sql_injectio_rule10": "[\"|\'|\"\)|\'\)]?\s?(?i)or\strue\-\-",
"sql_injectio_rule11": "[\"|\']\)?\)?\s(?i)or\s\(?\(?[\"|\'][a-zA-Z][\"|\']\)?\)?\=[\"|\']\(?\(?[a-zA-Z]",
"sql_injectio_rule12": "(?i)or\s2\s(?i)like\s2(?i)or\s1\=1",
"sql_injectio_rule13": "(?i)or\s1\=1[\-\-|\#|\/\*]",


}