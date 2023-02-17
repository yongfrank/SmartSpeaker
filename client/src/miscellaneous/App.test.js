/*
 * @Author: Frank Chu
 * @Date: 2023-02-16 19:34:04
 * @LastEditors: Frank Chu
 * @LastEditTime: 2023-02-17 01:23:14
 * @FilePath: /SmartSpeaker/client/src/misc/App.test.js
 * @Description: 
 * 
 * Copyright (c) 2023 by ${git_name}, All Rights Reserved. 
 */
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
