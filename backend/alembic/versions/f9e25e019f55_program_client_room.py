"""program_client_room

Revision ID: f9e25e019f55
Revises: 373ca5853d12
Create Date: 2024-11-30 14:20:55.420882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9e25e019f55'
down_revision: Union[str, None] = '373ca5853d12'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('program_client_room',
    sa.Column('program_client_id', sa.Integer(), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=False),
    sa.Column('enty_date', sa.Date(), nullable=False),
    sa.Column('departue_date', sa.Date(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['program_client_id'], ['program_clients.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['hotel_rooms.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('program_client_id', 'room_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('program_client_room')
    # ### end Alembic commands ###