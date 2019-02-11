import click
import json
import pandas as pd


@click.command()
@click.argument('json_file', type=click.File('r'))
@click.argument('destination_file', type=click.Path(exists=False))
def parse(json_file, destination_file):
    data = json.load(json_file)
    fields = []
    options = []
    for q in data:
        # parse field attrs and add to `fields`
        f_attrs = {}
        f_columns = ['name', 'label', 'displayType', 'renderAs']
        for c in f_columns:
            f_attrs[c] = q.get(c)
            f_attrs['options'] = len(q['options']) or None
        fields.append(f_attrs)

        # parse options (if any) and append to `options`
        if q.get('options'):
            for o in q['options']:
                o_attrs = {}
                o_attrs['field_name'] = q.get('name')
                for k,v in o.items():
                    o_attrs[k] = v
                options.append(o_attrs)

    # write values to excel workbook at destination_file path
    writer = pd.ExcelWriter(click.format_filename(destination_file))
    field_df = pd.DataFrame(fields)
    opt_df = pd.DataFrame(options)
    field_df.to_excel(writer, sheet_name='Fields', index=False)
    opt_df.to_excel(writer, sheet_name='Choices', index=False)
    writer.save()

    print(f'Saved output to {click.format_filename(destination_file)}')

if __name__ == '__main__':
    parse()
