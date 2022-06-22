"""Projects_table

Revision ID: efe3961d2276
Revises: a5fc5be65bba
Create Date: 2022-06-22 12:27:14.671359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efe3961d2276'
down_revision = 'a5fc5be65bba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('project_group_number', sa.Integer(), nullable=True),
    sa.Column('closed_date', sa.DateTime(), nullable=True),
    sa.Column('contact_person_id', sa.Integer(), nullable=True),
    sa.Column('cost_price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('customer_number', sa.Integer(), nullable=True),
    sa.Column('delivery_date', sa.DateTime(), nullable=True),
    sa.Column('delivery_location_number', sa.Integer(), nullable=True),
    sa.Column('department_number', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('fixed_price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('invoiced_total', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('is_barred', sa.Boolean(), nullable=True),
    sa.Column('is_closed', sa.Boolean(), nullable=True),
    sa.Column('is_main_project', sa.Boolean(), nullable=True),
    sa.Column('is_mileage_invoiced', sa.Boolean(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.Column('main_project_number', sa.Integer(), nullable=True),
    sa.Column('mileage', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('object_version', sa.String(length=255), nullable=True),
    sa.Column('other_responsible_employeeNumber', sa.String(length=255), nullable=True),
    sa.Column('responsible_employee_number', sa.String(length=255), nullable=True),
    sa.Column('sales_price', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###