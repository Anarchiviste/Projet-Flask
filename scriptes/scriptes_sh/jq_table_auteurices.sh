jq -r '.notices[] | [ .id, .internal.digest.authorName, .internal.digest.title, .internal.digest.endDate.earliest]| @csv'

