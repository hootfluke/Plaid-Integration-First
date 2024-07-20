import React, { Component } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label,
} from "reactstrap";

export default class CustomModal extends Component {
    constructor(props) {
        super(props);
        this.state = {
            activeItem: this.props.activeItem,
        };
    }

    render() {
        const { toggle, onSave } = this.props;

        return (
            <Modal isOpen={true} toggle={toggle}>
                <ModalHeader toggle={toggle}>User Form</ModalHeader>
                <ModalBody>
                    <Form>
                        <FormGroup>
                            <Label for="form-name">Name</Label>
                            <Input
                                type="text"
                                id="form-name"
                                name="name"
                                value={this.state.activeItem.name}
                                placeholder="Enter Name"
                            />
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button
                        color="success"
                        onClick={() => onSave(this.state.activeItem)}
                    >
                        Submit
                    </Button>
                </ModalFooter>
            </Modal>
        )
    }
}