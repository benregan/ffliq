"""Template example for manual migrations.

Revision ID: template_example
Create Date: Manual template
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
down_revision = 'previous_migration_id'  # Change this for actual migrations
revision = 'template_example'  # Change this for actual migrations
branch_labels = None
depends_on = None

def upgrade():
    # Example: Add a new column
    op.add_column('table_name', sa.Column('new_column', sa.String(50)))
    
    # Example: Create a new table
    op.create_table(
        'new_table',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )
    
    # Example: Add a foreign key
    op.add_column('table_name', sa.Column('related_id', sa.Integer))
    op.create_foreign_key(
        'fk_table_related',
        'table_name', 'related_table',
        ['related_id'], ['id']
    )

def downgrade():
    # Example: Remove foreign key
    op.drop_constraint('fk_table_related', 'table_name', type_='foreignkey')
    op.drop_column('table_name', 'related_id')
    
    # Example: Drop table
    op.drop_table('new_table')
    
    # Example: Remove column
    op.drop_column('table_name', 'new_column')
