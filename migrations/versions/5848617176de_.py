"""empty message

Revision ID: 5848617176de
Revises: 
Create Date: 2021-02-27 21:35:03.419076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5848617176de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('contact_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('contact_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('genders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('outreach_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('races',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('resources',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('phone_number', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('personal_website', sa.String(length=255), nullable=True),
    sa.Column('ad_age', sa.Integer(), nullable=True),
    sa.Column('suspected_age', sa.Integer(), nullable=True),
    sa.Column('client_status_id', sa.Integer(), nullable=True),
    sa.Column('gender_id', sa.Integer(), nullable=True),
    sa.Column('race_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_status_id'], ['client_statuses.id'], ),
    sa.ForeignKeyConstraint(['gender_id'], ['genders.id'], ),
    sa.ForeignKeyConstraint(['race_id'], ['races.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('logo_url', sa.String(length=255), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('outreach_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['outreach_type_id'], ['outreach_types.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('advertisements',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scraped_at', sa.DateTime(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('job_title', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.Column('confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_at', sa.DateTime(), nullable=True),
    sa.Column('current_login_at', sa.DateTime(), nullable=True),
    sa.Column('last_login_ip', sa.String(length=255), nullable=True),
    sa.Column('current_login_ip', sa.String(length=255), nullable=True),
    sa.Column('login_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organizations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity_logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('log_type', sa.String(length=255), nullable=False),
    sa.Column('phone_number_used', sa.String(length=50), nullable=True),
    sa.Column('email_used', sa.String(length=50), nullable=True),
    sa.Column('is_safe', sa.Boolean(), nullable=True),
    sa.Column('live_locally', sa.Boolean(), nullable=True),
    sa.Column('name_reported', sa.String(length=50), nullable=True),
    sa.Column('age_reported', sa.Integer(), nullable=True),
    sa.Column('wants_followups', sa.Boolean(), nullable=True),
    sa.Column('notes', sa.String(length=255), nullable=True),
    sa.Column('call_time', sa.DateTime(), nullable=False),
    sa.Column('call_duration', sa.Integer(), nullable=True),
    sa.Column('contact_type_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], ),
    sa.ForeignKeyConstraint(['contact_type_id'], ['contact_types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ads_photographs',
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('ad_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ad_id'], ['advertisements.id'], ),
    sa.ForeignKeyConstraint(['client_id'], ['clients.id'], )
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('activity_resources',
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activity_logs.id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.id'], )
    )
    op.create_table('activity_results',
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.Column('result_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activity_logs.id'], ),
    sa.ForeignKeyConstraint(['result_id'], ['contact_results.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('activity_results')
    op.drop_table('activity_resources')
    op.drop_table('roles_users')
    op.drop_table('ads_photographs')
    op.drop_table('activity_logs')
    op.drop_table('users')
    op.drop_table('advertisements')
    op.drop_table('organizations')
    op.drop_table('clients')
    op.drop_table('roles')
    op.drop_table('resources')
    op.drop_table('races')
    op.drop_table('outreach_types')
    op.drop_table('genders')
    op.drop_table('contact_types')
    op.drop_table('contact_results')
    op.drop_table('client_statuses')
    # ### end Alembic commands ###