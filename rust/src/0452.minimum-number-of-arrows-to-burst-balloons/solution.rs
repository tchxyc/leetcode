// Created by Jones at 2024/03/18 14:06
// leetgo: 1.4.2
// https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/

use anyhow::Result;
use leetgo_rs::*;

struct Solution;

// @lc code=begin
use std::cmp::Reverse;
use std::collections::*;
use std::mem::swap;

impl Solution {
    pub fn find_min_arrow_shots(points: Vec<Vec<i32>>) -> i32 {
        let mut a = points;
        a.sort_unstable_by_key(|e| e[1]);
        let n = a.len();
        let mut i = 0;
        let mut res = 0;
        while i < n {
            let end = a[i][1];
            let mut j = i + 1;
            while j < n && a[j][0] <= end {
                j += 1;
            }
            res += 1;
            i = j
        }
        res
    }
}

// @lc code=end

fn main() -> Result<()> {
    let points: Vec<Vec<i32>> = deserialize(&read_line()?)?;
    let ans: i32 = Solution::find_min_arrow_shots(points).into();

    println!("\noutput: {}", serialize(ans)?);
    Ok(())
}