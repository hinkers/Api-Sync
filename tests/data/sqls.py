sql1 = {
    'connection_string': 'sqlite:///:memory:',
    'create_tables': True,
    'relationships': {
      'one_to_one': ['Source.news_id -> News.id'],
    },
    'tables': [
        {
            'name': 'News',
            'primary_key': 'id',
            'columns': {
                'id': 'Integer',
                'title': 'String',
                'description': 'String',
                'content': 'String',
                'url': 'String',
                'image': 'String',
                'published_at': 'DateTime'
            }
        },
        {
            'name': 'Source',
            'primary_key': 'id',
            'columns': {
                'id': 'Integer',
                'news_id': 'Integer',
                'name': 'String',
                'url': 'String'
            }
        }
    ]
}
